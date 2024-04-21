class Drop {
    constructor(xPos, yPos, speed, width, height) {
        this.xPosition = xPos;
        this.yPosition = yPos;
        this.dropSpeed = speed;
        this.dropWidth = width;
        this.dropHeight = height;
        this.element;
    }

    show() {
        this.element = document.createElement('div');
        this.element.className = 'rain-drop';
        this.element.style.top = this.yPosition + "px";
        this.element.style.left = this.xPosition + "px";
        this.element.style.width = this.dropWidth + "px";
        this.element.style.height = this.dropHeight + "px";
        this.element.style.backgroundColor = "white";
        // console.log(this.element);

        var displayDrop = document.getElementById("drop");
        // console.log(displayDrop);
        displayDrop.appendChild(this.element);
    }

    fall() {
        const generateDrops = () => {
            this.yPosition = this.yPosition + this.dropSpeed;
            this.element.style.top = this.yPosition + "px";

            if (this.yPosition < window.innerHeight) {
                requestAnimationFrame(generateDrops);
            }
            else {
                this.yPosition = 0;
                requestAnimationFrame(generateDrops);
            }
        }
        requestAnimationFrame(generateDrops);
    }
}