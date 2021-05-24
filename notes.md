## Dev Notes


## Code Practices
Where possible we will explore the following conventions

- Type hinting with python (i.e. add types for method variables and return types)
- Code formatter - Black


## Todos
- Localizer
  - Formalize evaluation code harness and plot charts for multiple localizer models and their performance
  - Find new examples of image data with signatures
- Data
  - Write a datasheet document for how each of the models are trained 


## E2E Example 
- Signature Search
  - Extract signatures from a bunch of documents
  - Add signatures to an index 
  - Enable signature-based document retrieval 
- Signature Verification
  - Given two images of signatures, return if they are the same or fraud?
- Signature ID
  - Extract signatures and add to index with an id
  - Return id given a signature