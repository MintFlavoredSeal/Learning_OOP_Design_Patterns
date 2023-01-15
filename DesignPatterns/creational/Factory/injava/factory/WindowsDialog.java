package creational.Factory.injava.factory;

import creational.Factory.injava.button.Button;
import creational.Factory.injava.button.WindowsButton;

/**
 * Windows Dialog will produce Windows buttons.
 */
public class WindowsDialog extends Dialog {

    @Override
    public Button createButton() {
        return new WindowsButton();
    }
}
