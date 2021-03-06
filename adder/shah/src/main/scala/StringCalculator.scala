case class StringCalculator(input: String) {

  val DEFAULT_DELIMITER = ","
  val NEW_LINE = "\n"
  val CUSTOM_DELIMITER_MARKER = "//"
  val MAXIMUM_ADDEND = 1000

  def add: Int = if (input == "") 0 else sumOrThrow(numbersFrom(input))

  private def sumOrThrow(numbersFromInput : Seq[Int]) : Int = {
    val negativeNumbers = numbersFromInput.filter(_ < 0)
    if(negativeNumbers.isEmpty) {
      numbersFromInput.sum
    }else {
      throw new Exception(s"Negatives not allowed: ${negativeNumbers.mkString(",")}")
    }
  }

  private def numbersFrom(input: String): Seq[Int] = {
    changeToDelimiter(input)
      .replace(NEW_LINE, DEFAULT_DELIMITER)
      .split(DEFAULT_DELIMITER)
      .filterNot(_.isEmpty)
      .map(_.toInt)
      .filter(_ <= MAXIMUM_ADDEND)
  }

  private def changeToDelimiter(input: String): String = {
    val potentialDelimiter = input.stripPrefix(CUSTOM_DELIMITER_MARKER).charAt(0)
    if (potentialDelimiter.isDigit) {
      input
    } else if (potentialDelimiter == '[') {
      val cleanedInput = (input::findAllCustomDelimitersIn(input)). map(removeBracketsFrom).reduce[String]((acc,next) => acc.replace(next,","))
      removeBracketsFrom(cleanedInput).replace(CUSTOM_DELIMITER_MARKER,"")
    } else {
      input.stripPrefix(CUSTOM_DELIMITER_MARKER + potentialDelimiter).replace(potentialDelimiter.toString,DEFAULT_DELIMITER)
    }
  }

  def findAllCustomDelimitersIn(input :String) : List[String] = """\[[^\]]+\]""".r findAllIn input toList

  def removeBracketsFrom(input :String) = input.replace("]","").replace("[","")
}
