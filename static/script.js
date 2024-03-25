const userData = document.getElementById('inputs');
const missing_value = userData.dataset.missing_value;
const hashmapString = userData.dataset.dict;
const hashmap = JSON.parse(hashmapString);
console.log(hashmap);
console.log(missing_value);
const keys = Object.keys(hashmap);
console.log(keys);

const userSet = new Set(keys);
userSet.add(missing_value);

console.log(userSet);