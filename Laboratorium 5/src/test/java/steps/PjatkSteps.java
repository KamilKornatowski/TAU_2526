package steps;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;


import static org.junit.jupiter.api.Assertions.assertEquals;

public class PjatkSteps {

    WebDriver driver;

    @Given("I open the PJATK website in {string}")
    public void i_open_the_pjatk_website_in(String browser) {
        if (browser.equalsIgnoreCase("chrome")) {
            System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");
            WebDriverManager.chromedriver().setup();
            driver = new ChromeDriver();
        } else if (browser.equalsIgnoreCase("firefox")) {
            System.setProperty("webdriver.gecko.driver", "path/to/geckodriver.exe");
            WebDriverManager.firefoxdriver().setup();
            driver = new FirefoxDriver();

        }
        driver.get("https://www.pja.edu.pl");
    }

    @When("I accept cookies if visible")
    public void i_accept_cookies_if_visible() {
        try {
            WebElement cookiesButton = driver.findElement(By.cssSelector(
                    "body > div.popup.popup--cookies.popup--active > div > div > div > div:nth-child(3) > button"
            ));

            ((JavascriptExecutor) driver).executeScript("arguments[0].click();", cookiesButton);
        } catch(Exception e) {

        }
    }

    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

    @And("I go to the contact page")
    public void i_go_to_the_contact_page() {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {

            wait.until(ExpectedConditions.invisibilityOfElementLocated(By.cssSelector(".popup-inner")));
        } catch (TimeoutException e) {

        }


        WebElement contactLink = driver.findElement(By.linkText("Kontakt"));

        // Scroll
        try {
            ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", contactLink);
            contactLink.click();
        } catch (ElementClickInterceptedException e) {
            ((JavascriptExecutor) driver).executeScript("arguments[0].click();", contactLink);
        }
    }

    @Then("I should see the address {string}")
    public void i_should_see_the_address(String expectedAddress) {
        WebElement addressElement = driver.findElement(
                By.xpath("//*[text()='" + expectedAddress + "']")
        );
        String actualAddress = addressElement.getText();
        assertEquals(expectedAddress, actualAddress);
        driver.quit();
    }
}