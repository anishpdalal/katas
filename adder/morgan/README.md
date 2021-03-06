# String Calculator Kata

## Git Crawl
  Use [Git Crawl](https://github.com/magnusstahre/git-stuff) to checkout the TDD cycles.

  `$ git checkout c1ce5b059959b5d2e28547f8d0e9b50e25160371`

  `$ git crawl 85f29daf1dccd5e646a66e5680651b12b2e9065b`

## TODO
  - Move normalizing functionality tests.
  - Delimiters can be of any length with the following format: `“//[delimiter]\n” `
    - Example: `//[^^^]\n1^^^2^^^3` should return 6
  - Allow multiple delimiters like this: ``//[delim1][delim2]\n``
    - Example ``//[*][%]\n1*2%3`` should return 6.
  - Make sure you can also handle multiple delimiters with length longer than one char

## Retrospective
  - I really wanted to focus on clear naming, and I am not sure I was successful.
  - Would love to see tests wrapped around just the normalizing functionality
  - I am not sure all my private methods are providing clarity.
  - I think it would turn out better with a pair.

## Thoughts?

## Run the specs

  `$ bundle install`

  `$ rake spec`
