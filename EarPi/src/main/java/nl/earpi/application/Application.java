package nl.earpi.application;

import nl.earpi.generated.earpi.DeviceTokenInput;
import nl.earpi.generated.earpi.LoginInputObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

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

    @RequestMapping("/")
    public String home() {
        return "Response in slash";
    }

    @RequestMapping("/device-registration")
    public String deviceRegistration() {
        LoginInputObject loginObject = new LoginInputObject();
        DeviceTokenInput deviceTokenInput = new DeviceTokenInput();
        loginObject.setDeviceInput(deviceTokenInput);
        loginObject.getDeviceInput().setIp("localhost");
        loginObject.getDeviceInput().setDevicetype("MyLaptop");
        loginObject.getDeviceInput().setPerson("The Devil");
        loginObject.getDeviceInput().setUserAgent("user agent");

        shortTermConnectClient.RegisterDevice(loginObject.getDeviceInput());
        return "Response in slash";
    }

    @RequestMapping("/configure")
    public String configure() {
        String deviceToken = shortTermConnectClient.GetDeviceToken();

        return "Response in slash";
    }

    @RequestMapping("/autorize")
    public String autorize() {
        String deviceToken = shortTermConnectClient.GetDeviceToken();

        return "Response in slash";
    }

    @RequestMapping("/health")
    public boolean healthCheck() {
        return true;
    }

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }


}
