// Expressions: Optional chaining operator
const adventurer = {
  name: 'Alice',
  cat: {
    name: 'Dinah'
  }
};

const dogName = adventurer.dog?.name;
// expected output: undefined
console.log(dogName);
// expected output: undefined
console.log(adventurer.someNonExistentMethod?.());
