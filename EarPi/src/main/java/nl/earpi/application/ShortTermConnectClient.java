package nl.earpi.application;

import nl.earpi.generated.shortmemory.DeviceTokenInput;
import nl.earpi.generated.shortmemory.ShortMemoryService;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.springframework.beans.factory.annotation.Autowired;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;


public class ShortTermConnectClient {

    private static final String FILE_PATH = "./deviceToken.txt";
    private static final Path PATH = Paths.get(FILE_PATH);
//    private static final String SERVICE_NAME = "short-term-memory";
    private static final String SERVICE_NAME = "short-term-memory.service.consul.";

    @Autowired
    private static org.springframework.cloud.client.discovery.DiscoveryClient client;

    private String GetDeviceToken() {
        try (Stream<String> stream = Files.lines(PATH)) {
            return stream
                    .map(String::toUpperCase)
                    .reduce((first, second) -> second)
                    .orElse(null);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void RegisterDevice(nl.earpi.generated.earpi.DeviceTokenInput deviceTokenInput) {
        if (GetDeviceToken() == null) {
            try {
                TTransport transport;
                org.springframework.cloud.client.ServiceInstance serviceInstance =
                        client.getInstances(SERVICE_NAME)
                                .stream()
                                .findAny()
                                .orElse(null);

                transport = new TSocket(serviceInstance.getHost(), serviceInstance.getPort());
                transport.open();
                TProtocol protocol = new TBinaryProtocol(transport);
                ShortMemoryService.Client client = new ShortMemoryService.Client(protocol);
                String deviceToken = client.generateDeviceToken(generateDeviceTokenInput(deviceTokenInput));
                if (deviceToken != null) {
                    StoreDeviceTokenToDisk(deviceToken);
                }
                transport.close();
            } catch (TException x) {
                x.printStackTrace();
            }
        }
    }

    private DeviceTokenInput generateDeviceTokenInput(nl.earpi.generated.earpi.DeviceTokenInput deviceTokenInput) {
        DeviceTokenInput deviceInput = new DeviceTokenInput();
        deviceInput.setDevicetype("myLaptop");
        return deviceInput;
    }

    private void StoreDeviceTokenToDisk(String token) {
        try (BufferedWriter writer = Files.newBufferedWriter(PATH))
        {
            writer.write(token);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
