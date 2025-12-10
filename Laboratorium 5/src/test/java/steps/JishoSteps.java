package steps;

import io.cucumber.java.en.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class JishoSteps {

    private WebDriver driver;
    private WebDriverWait wait;

    @Given("I open the Jisho website in {string}")
    public void i_open_the_jisho_website_in(String browser) {
        if (browser.equalsIgnoreCase("chrome")) {
            driver = new ChromeDriver();
        } else if (browser.equalsIgnoreCase("firefox")) {
            driver = new FirefoxDriver();
        } else {
            throw new IllegalArgumentException("Unsupported browser: " + browser);
        }
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.manage().window().maximize();
        driver.get("https://jisho.org");
    }

    @When("I search for the word {string}")
    public void i_search_for_the_word(String word) {
        WebElement searchBox = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("keyword")));
        searchBox.sendKeys(word);
        searchBox.sendKeys(Keys.RETURN);
    }

    @Then("I should see at least one result")
    public void i_should_see_at_least_one_result() {
        wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector(".concept_light.clearfix a")));
        System.out.println("Test zakończony – słowo wyszukane");
        driver.quit();
    }
}