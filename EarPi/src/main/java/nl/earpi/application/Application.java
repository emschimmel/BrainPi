package nl.earpi.application;

import nl.earpi.generated.earpi.LoginInputObject;
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

    ShortTermConnectClient shortTermConnectClient = new ShortTermConnectClient();

    @RequestMapping("/")
    public String home() {
        return "Response in slash";
    }

    @RequestMapping("/device-registration")
    public String deviceRegistration() {
        LoginInputObject loginObject = new LoginInputObject();
        loginObject.getDeviceInput().setIp("localhost");
        loginObject.getDeviceInput().setDevicetype("MyLaptop");
        loginObject.getDeviceInput().setPerson("The Devil");
        loginObject.getDeviceInput().setUserAgent("user agent");

        shortTermConnectClient.RegisterDevice(loginObject.getDeviceInput());
        return "Response in slash";
    }

    @RequestMapping("/configure")
    public String configure() {

        return "Response in slash";
    }

    @RequestMapping("/autorize")
    public String autorize() {

        return "Response in slash";
    }

    public static void main(String[] args) {
        LoginInputObject loginInputObject = new LoginInputObject();
        // LoginInputObject loginInputObject = new LoginInputObject();
        SpringApplication.run(Application.class, args);
    }


}
