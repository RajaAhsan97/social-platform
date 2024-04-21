
const width = window.innerWidth;
const height = window.innerHeight;
const noOfDrops = 400;

function generateDrops(dropsCount) {


    for (var i=0; i<dropsCount; i++) {
        // console.log(i);
        var dropXPosition = Math.floor(Math.random() * width);
        var dropYPosition = Math.floor(Math.random() * height);
        var dropSpeed = Math.floor(Math.random() * 5);
        var dropWidth = Math.floor(Math.random()) + 2;
        var dropHeight = Math.floor(Math.random() * (dropSpeed/5)) + 5;
        // console.log(dropXPosition, dropYPosition, dropSpeed, dropWidth, dropHeight);

        var DropObject = new Drop(dropXPosition, dropYPosition, dropSpeed, dropWidth, dropHeight);
        // console.log(DropObject);

        DropObject.show();
        DropObject.fall();
    }
}

generateDrops(noOfDrops);