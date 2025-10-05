import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


public class UnitTests {

VariousOperations operations = new VariousOperations();

    @Test
    void testObjectExists() {
        assertNotNull(operations);
    }

    @Test
    void addition() {
        assertEquals(2, operations.Add(1, 1));
    }
    @Test
    void additionSigned() {
        assertEquals(0, operations.Add(1, -1));
    }

    @Test
    void evenCheckerTest() {
        assertTrue(operations.EvenChecker(2));
        assertFalse(operations.EvenChecker(311));
    }

    @Test
    void celsiusTest() {
        assertEquals(169, operations.CelsiusToFahrenheit(76));
        assertEquals(32, operations.CelsiusToFahrenheit(0));
    }



}
