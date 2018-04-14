package main

import (
	"html/template"
	"log"
    "net/http"
    "generated/earpi"
    "generated/exception"
    "git.apache.org/thrift.git/lib/go/thrift"
	"github.com/benschw/srv-lb/lb"
    "net"
    "fmt"
	"github.com/benschw/srv-lb/dns"
	"github.com/benschw/srv-lb/strategy/random"
	"context"
	"strconv"
)

type Address struct {
	IP 				string
	Port    		string
}

//type DeviceTokenInput struct {
//	Token           string           `json:"Token"`
//	Ip              string           `json:"Ip"`
//	Devicetype      string           `json:"Devicetype"`
//	UserAgent       string           `json:"UserAgent"`
//	Person          string           `json:"Person"`
//	Enabled         string           `json:"Enabled"`
//}

func main() {
    http.HandleFunc("/", DeviceTokenListHandler)
    http.ListenAndServe("0.0.0.0:8000", nil)
}

func DeviceTokenListHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Add("Content Type", "text/html")

    var deviceListOutput = earpi.DeviceListOutput{}
    var deviceList = map[string]*earpi.DeviceTokenInput{}
    runEarpiClient(thrift.NewTBufferedTransportFactory(100), thrift.NewTBinaryProtocolFactory(false, false), &deviceListOutput)
	deviceList = deviceListOutput.DeviceList
	fmt.Print(len(deviceList))
    //jsonErr := json.Unmarshal(body, &deviceList)
    //if jsonErr != nil {
    //    log.Fatal(jsonErr)
    //}

    HtmlTemplate, err := template.ParseFiles("main.html")
    if err != nil {
        log.Print("template parsing error: ", err)
    }
	HtmlTemplate.Execute(w, deviceList)

}

func runEarpiClient(transportFactory thrift.TTransportFactory, protocolFactory thrift.TProtocolFactory, DeviceListOutput *earpi.DeviceListOutput) (err error) {
	var transport thrift.TTransport
	address := Address{}
	resolve_ear_config(address)
	transport, err = thrift.NewTSocket(net.JoinHostPort(address.IP, address.Port))
	if err != nil {
		fmt.Println("Error opening socket:", err)
		return err
	}
	transport, err = transportFactory.GetTransport(transport)
	if err != nil {
		return err
	}
	defer transport.Close()
	if err := transport.Open(); err != nil {
		return err
	}
	iprot := protocolFactory.GetProtocol(transport)
	oprot := protocolFactory.GetProtocol(transport)
	err = handleClient(earpi.NewEarPiThriftServiceClient(thrift.NewTStandardClient(iprot, oprot)), DeviceListOutput)
	if err != nil {
		fmt.Print(err)
	}
	return nil
}

func handleClient(client *earpi.EarPiThriftServiceClient, result *earpi.DeviceListOutput) (err error) {

	earPiAuthObject := earpi.NewEarPiAuthObject()
	earPiAuthObject.Token = "1234"
	earPiAuthObject.DeviceToken = "1234"
	var defaultCtx = context.Background()
	result, err = client.GetDeviceList(defaultCtx, earPiAuthObject)
	fmt.Print(result)

	if err != nil {
		switch v := err.(type) {
		case *exception.LoginFailedException:
			fmt.Println("Login fail:", v)
		default:
			fmt.Println("Error during operation:", err)
		}
		return err
	} else {
		fmt.Println("Whoa we can divide by 0 with new value:", result)
		return nil
	}
}

func resolve_ear_config (config Address) {
	config = Address{}
	srvName := "ear-pi.service.consul."
	cfg := &lb.Config{
		Dns:      dns.NewLookupLib("127.0.0.1:8600"),
		Strategy: random.RandomStrategy,
	}
	l := lb.New(cfg, srvName)
	fmt.Println(l)
	result, err := l.Next()
	if err != nil {
		fmt.Println("friendly error before panic")
		panic(err)
	}
	config.IP = result.Address
	config.Port = strconv.Itoa(int(result.Port))
}
