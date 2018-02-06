package nl.earpi.application;

import jdk.jfr.ContentType;
import nl.earpi.generated.earpi.DeviceTokenInput;
import nl.earpi.generated.earpi.LoginInputObject;
import nl.earpi.generated.earpi.LoginOutputObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Configuration
@EnableDiscoveryClient
@EnableAutoConfiguration
@SpringBootApplication
@RestController
public class Application {

    // - Configure user management
    // - Configure module management
    // - Autorization (write mode)
    // - Entry point for device registration

    @Autowired
    private ShortTermConnectClient shortTermConnectClient;

    @Autowired
    private LongTermConnectClient longTermConnectClient;

    @GetMapping("/")
    public String home() {
        return "Response in slash";
    }


    @PostMapping("/login")
    public ResponseEntity login(@RequestBody LoginInputObject loginInputObject) {
        LoginOutputObject output = longTermConnectClient.makeLoginCall(loginInputObject);
        return new ResponseEntity<LoginOutputObject> (output, HttpStatus.OK);
    }

//    @GetMapping("/device-registration")
//    public String deviceRegistration() {
//        DeviceTokenInput deviceTokenInput = new DeviceTokenInput();
//        deviceTokenInput.setIp("localhost");
//        deviceTokenInput.setDevicetype("MyLaptop");
//        deviceTokenInput.setPerson("The Devil");
//        deviceTokenInput.setUserAgent("user agent");
//
//        shortTermConnectClient.RegisterDevice(deviceTokenInput);
//        return "Response in slash";
//    }

    @GetMapping("/configure-user")
    public String configureUser() {

        return "Response in slash";
    }

    @GetMapping("/configure-module")
    public String configureModule() {

        return "Response in slash";
    }

    @GetMapping("/autorize")
    public String autorize() {

        return "Response in slash";
    }

    @GetMapping("/health")
    public boolean healthCheck() {
        return true;
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }


}
