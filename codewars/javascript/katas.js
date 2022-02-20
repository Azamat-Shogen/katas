
//TODO: There is an array with some numbers. All numbers are equal except for one
function findUniq(arr){
    return arr.filter(el => arr.indexOf(el) === arr.lastIndexOf(el))[0];
}

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55