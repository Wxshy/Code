import image from './assets/about-picture.jpg';
import './about.css';

function About(){
    return(
        <div id="about">
            <h1>This Is Me</h1><img src={image} alt="Myself" id="about-image"/>
            <p>Hello There, I am a college student in the UK studying Computer Science, Physical Education and Psyhcology. I am going to university in september of 2021 to study Software Engineering.
                <br/> <br/>99% of my life is sport, whether it is tackling people in hockey, scoring sixes in cricket or climbing hills on my bike - if it 's sports i'll be there! I was fortunate enought to have played for the England Under 16s squad in the
                2018/19 season where we won the Home Nations. I am also an avid cyclist and plan to go over into Europe and take on some climbs. I do also love to play cricket from time to time as it gives me some rest and able to socialise while playing.
                <br/><br/> The other 1% of my free-time is taken up by programming. I started off programming in Year 10 where I learned the basics of Python, which has become my main language as I feel comforatble with the syntax and have learned some of it
                's libraries. I am now trying to branch of into other areas such as web design - which is how this website came about by using HTML, CSS & JS. I am also starting to learn C++ to expand my knowledge.</p>
            <h3>Sponsored by <a href="http://grays-hockey.com"><em>Grays Hockey</em></a></h3>
        </div>
    )
}

export default About;