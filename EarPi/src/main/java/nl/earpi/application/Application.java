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

    @Autowired
    private LongTermConnectClient longTermConnectClient;

    @RequestMapping("/")
    public String home() {
        return "Response in slash";
    }

    @RequestMapping("/login")
    public String login() {
        LoginInputObject loginInputObject = new LoginInputObject();
        longTermConnectClient.makeLoginCall(loginInputObject);
        return "Response in slash";
    }

    @RequestMapping("/device-registration")
    public String deviceRegistration() {
        DeviceTokenInput deviceTokenInput = new DeviceTokenInput();
        deviceTokenInput.setIp("localhost");
        deviceTokenInput.setDevicetype("MyLaptop");
        deviceTokenInput.setPerson("The Devil");
        deviceTokenInput.setUserAgent("user agent");

        shortTermConnectClient.RegisterDevice(deviceTokenInput);
        return "Response in slash";
    }

    @RequestMapping("/configure-user")
    public String configureUser() {

        return "Response in slash";
    }

    @RequestMapping("/configure-module")
    public String configureModule() {

        return "Response in slash";
    }

    @RequestMapping("/autorize")
    public String autorize() {

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
