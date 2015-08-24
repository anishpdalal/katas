package kata.adder;

/**
 * Created by david on 8/24/15.
 */
public class StringCalculator implements Calculator {

    private String rawInput = "";

    @Override
    public int add(String input) {
        int calculatedValue = 0;
        rawInput = input;

        if (inputIsNotEmpty()) {
            String delimiter = determineAndStripDelimiter();
            String[] inputStrings = rawInput.split(delimiter);

            for (int i = 0; i < inputStrings.length; i++) {
                calculatedValue += Integer.valueOf(inputStrings[i]);
            }
        }

        return calculatedValue;
    }

    private boolean inputIsNotEmpty() {
        return !"".equals(rawInput); //normally I would check for null, but the kata says don't worry about it
    }

    private String determineAndStripDelimiter() {
        String result = ",|\n"; //The instructions implied that even with a new delimeter, I would have to handle the other cases
        if (rawInput.startsWith("//")) {
            rawInput = rawInput.substring(2);
            result+=("|" + rawInput.charAt(0));
            rawInput = rawInput.substring(2); //have to move past the delimeter and the newline
        }

        return result;
    }
}
