let count = 0;
let i = 0;
while (i < 100){
    i ++;
    
    var ran1 =  Math.round(Math.random() * 100);
    var ran2 =  Math.round(Math.random() * 100);

    console.log(ran1);
    console.log(ran2);

    if (ran1 === ran2){
        console.log('Correct');
        count ++;
        console.log(`You have ${count} Points!`);
    } else {
        console.log('Incorrect');
        console.log(`You have ${count} Points!`);
    };
};