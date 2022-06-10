const  w = 100;
const handleSlideRange = (e) => {
    const picture1 = document.getElementById('picture1')
    const picture2 = document.getElementById('picture2')
    
    const ratio = e.value / 100
    
    picture1.style.clip = `rect(0,${250 * ratio}px, auto, auto)`
    picture2.style.clip = `rect(0px,auto,auto,${250 * ratio}px)`
};
