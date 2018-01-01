package nl.earpi.application;

import nl.earpi.generated.earpi.LongMemoryService;
import nl.earpi.generated.earpi.LoginInputObject;
import nl.earpi.generated.earpi.LoginOutputObject;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.consul.discovery.ConsulDiscoveryClient;
import org.springframework.stereotype.Component;

@Component
public class LongTermConnectClient {

    private static final String SERVICE_NAME = "long-term-memory";

    private static ConsulDiscoveryClient client;

    @Autowired
    public LongTermConnectClient(ConsulDiscoveryClient consulDiscoveryClient) {
        client = consulDiscoveryClient;
    }

    public LoginOutputObject makeLoginCall(nl.earpi.generated.earpi.LoginInputObject earLoginObject) {
        return ConnectToLogIn(translateObject(earLoginObject));
    }

    private LoginInputObject translateObject(nl.earpi.generated.earpi.LoginInputObject earLoginObject) {
        LoginInputObject longmemoryLoginObject = new LoginInputObject();
        longmemoryLoginObject.setCode(earLoginObject.getCode());
        longmemoryLoginObject.setUsername(earLoginObject.getUsername());
        longmemoryLoginObject.setPassword(earLoginObject.getPassword());
        return longmemoryLoginObject;
    }

    /**
     * Thrift connect to validate the DeviceToken
     * @param longmemoryLoginObject login object with username + password
     * @return valide
     */
    private LoginOutputObject ConnectToLogIn(LoginInputObject longmemoryLoginObject) {
        LoginOutputObject output = new LoginOutputObject();
        try {
            TTransport transport;
            ServiceInstance serviceInstance =
                    client.getInstances(SERVICE_NAME)
                            .stream()
                            .findAny()
                            .orElse(null);
            transport = new TSocket(serviceInstance.getHost(), serviceInstance.getPort());
            transport.open();
            TProtocol protocol = new TBinaryProtocol(transport);
            LongMemoryService.Client client = new LongMemoryService.Client(protocol);
            output = client.loginCall(longmemoryLoginObject);

            transport.close();
        } catch (TException | NullPointerException x) {
            x.printStackTrace();
        }
        return output;
    }


}

