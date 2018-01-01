package nl.earpi.application;

import org.springframework.boot.context.embedded.ConfigurableEmbeddedServletContainer;
import org.springframework.boot.context.embedded.EmbeddedServletContainerCustomizer;
import org.springframework.stereotype.Component;

import java.util.Random;

@Component
public class CustomizationBean implements EmbeddedServletContainerCustomizer {

    private final int RANDOM_PORT;


    private CustomizationBean() {
        RANDOM_PORT = 8000 + new Random().nextInt(999);
    }

    @Override
    public void customize(ConfigurableEmbeddedServletContainer container) {
        container.setPort(RANDOM_PORT);
    }


}