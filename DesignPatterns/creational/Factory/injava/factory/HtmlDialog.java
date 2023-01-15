package creational.Factory.injava.factory;

import creational.Factory.injava.button.Button;
import creational.Factory.injava.button.HtmlButton;

/**
 * HTML Dialog will produce HTML buttons.
 */
public class HtmlDialog extends Dialog {

    @Override
    public Button createButton() {
        return new HtmlButton();
    }
}