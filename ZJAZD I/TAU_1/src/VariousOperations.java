import static java.lang.Math.round;

public class VariousOperations {


    public int Add(int a, int b) {
        return a+b;
    }

    public boolean EvenChecker(int a) {
        if (a % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }

    public float CelsiusToFahrenheit(int celsius) {
        return round((float) ((celsius * 1.8) + 32));
    }
}
