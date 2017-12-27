package nl.earpi.application;

import nl.earpi.generated.shortmemory.DeviceTokenInput;
import nl.earpi.generated.shortmemory.ShortMemoryService;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.consul.discovery.ConsulDiscoveryClient;
import org.springframework.stereotype.Component;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

@Component
public class ShortTermConnectClient {

    private static final String FILE_PATH = "./deviceToken.txt";
    private static final Path PATH = Paths.get(FILE_PATH);
    private static final String SERVICE_NAME = "short-term-memory";


    private static ConsulDiscoveryClient client;

    @Autowired
    public ShortTermConnectClient(ConsulDiscoveryClient consulDiscoveryClient) {
        client = consulDiscoveryClient;

    }

    /**
     * Provided the login is valid.
     * Check if there is a deviceToken stored on disk.
     * If present, check if valide. If not, get new token.
     * @param deviceTokenInput earpi.deviceTokenInput
     */
    public void RegisterDevice(nl.earpi.generated.earpi.DeviceTokenInput deviceTokenInput) {
        ConnectToRegisterToken(generateDeviceTokenInput(deviceTokenInput));
    }

    /**
     * validate if the token got from the request is valid
     * TODO Check: do I need this?
     * @param deviceToken String of the clients DeviceToken
     */
    public void ValidateDeviceToken(String deviceToken) {
        ConnectToValidateToken(deviceToken);
    }

    /**
     * Thrift connect to validate the DeviceToken
     * @param token String token from client request
     * @return valide
     */
    private boolean ConnectToValidateToken(String token) {
        boolean valide = false;
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
            ShortMemoryService.Client client = new ShortMemoryService.Client(protocol);
            valide = client.validateDeviceToken(token);

            transport.close();
        } catch (TException | NullPointerException x) {
            x.printStackTrace();
        }
        return valide;
    }

    /**
     * Thrift connect to register get a new token
     * @param deviceTokenInput shortmemory deviceTokenInput
     * @return the new DeviceToken
     */
    private String ConnectToRegisterToken(DeviceTokenInput deviceTokenInput) {
        String deviceToken = null;
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
            ShortMemoryService.Client client = new ShortMemoryService.Client(protocol);
            deviceToken = client.generateDeviceToken(deviceTokenInput);
            transport.close();
        } catch (TException x) {
            x.printStackTrace();
        }
        return deviceToken;
    }

    /**
     * Translate deviceTokenInput
     * @param deviceTokenInput earpi.DeviceTokenInput
     * @return shortmemory.DeviceTokenInput
     */
    private DeviceTokenInput generateDeviceTokenInput(nl.earpi.generated.earpi.DeviceTokenInput deviceTokenInput) {
        DeviceTokenInput deviceInput = new DeviceTokenInput();
        deviceInput.setDevicetype("myLaptop");
        deviceInput.setIp("127.0.0.1");
        return deviceInput;
    }

//    /**
//     * Store token on disc
//     * @param token deviceToken
//     */
//    private void StoreDeviceTokenToDisk(String token) {
//        try (BufferedWriter writer = Files.newBufferedWriter(PATH))
//        {
//            writer.write(token);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }

//    /**
//     * Get the devicetoken from disc
//     * @return devicetoken or null if not found
//     */
//    public String GetDeviceToken() {
//        try (Stream<String> stream = Files.lines(PATH)) {
//            return stream
//                    .map(String::toUpperCase)
//                    .reduce((first, second) -> second)
//                    .orElse(null);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//        return null;
//    }
}
