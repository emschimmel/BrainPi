package nl.earpi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import nl.earpi.generated.*;

@Configuration
@EnableDiscoveryClient
@EnableAutoConfiguration
@SpringBootApplication
@RestController
public class Application {

    @RequestMapping("/")
    public String home() {
        return "Response in slash";
    }

    public static void main(String[] args) {

        // LoginInputObject loginInputObject = new LoginInputObject();
        SpringApplication.run(Application.class, args);
    }
}
