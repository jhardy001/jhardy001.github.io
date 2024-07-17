/**
 * Create and return the model.  The model has the following properties:
 *      * schedule - Array of the student's currently enrolled courses
 *      * offerings - Array of the currently offered courses
 *      * prefixes - sorted Array of the unique prefixes contained in offerings
 *      * timeslots - sorted Array of the unique timeslots contained in offerings
 * @returns the model
 */
async function makeModel() {
    let model = new Object();

    // Course offerings
    const coursesURL = "https://phbrownacmorg.github.io/courses.json";
    const response = await fetch(coursesURL);
    model.offerings = await response.json();
    model.prefixes = await getUnique(model.offerings, 'prefix');
    model.timeslots = await getUnique(model.offerings, 'schedule');
    model.schedule = new StudentSchedule();

    // Load current schedule, if there is one, and store it in model.schedule
    // ADD CODE HERE
    if (localStorage.getItem('studentSchedule')){
        const storedList = JSON.parse(localStorage.getItem('studentSchedule'));
        model.schedule.schedule = model.schedule.schedule.concat(storedList);
    }

    return model;
}

/**
 * Initializes the page.
 */
async function initialize() {
    // Make the Model
    var model = await makeModel();
    console.log(model);

    // Make the View: ADD CODE HERE
    fillSelector(document.getElementById("prefix_dropdown"), model.prefixes, 'Please select a prefix.');
    fillSelector(document.getElementById("timeslot_dropdown"), model.timeslots, 'Please select a timeslot.');
    const schedule_view = new ScheduleView(model.schedule);

    document.getElementById("prefix_dropdown").addEventListener('change', ()=> fillCourseDropdown(model));
    document.getElementById("timeslot_dropdown").addEventListener('change', ()=> fillCourseDropdown(model));
    // Controller code: ADD CODE HERE
    document.getElementById("addCourseButton").addEventListener('click', ()=> addCourse(model));
}

function fillCourseDropdown(model){
    let prefix = document.getElementById('prefix_dropdown').value;
    let timeslot = document.getElementById('timeslot_dropdown').value;
    let courseDropdown = document.getElementById('course_dropdown');
    document.getElementById("addCourseButton").disabled = true;
    if (prefix === '' && timeslot === ''){
        courseDropdown.disabled = true;
        document.getElementById('addCourseButton').disabled = true;
    }
    else {
        courseDropdown.disabled = false;
        let matchingCourses = model.offerings;
        if (prefix != ''){
            matchingCourses = matchingCourses.filter((course)=> course['prefix'] === prefix);
        }
        if (timeslot != ''){
            // console.log(timeslot);
            matchingCourses = matchingCourses.filter((course)=> course['schedule'] === timeslot);
        }
        let courses = matchingCourses.map((course)=> course['course code'] + ',' + course['name']);
        fillSelector(courseDropdown, courses, 'Please select a course.');
    }
}

function enableAddButton(){
    if (document.getElementById("course_dropdown").value != ''){
        document.getElementById("addCourseButton").disabled = false;
    }
    else {
        document.getElementById("addCourseButton").disabled = true;
    }
}

function addCourse(model){
    let value = document.getElementById('course_dropdown').value;
    //console.log(value);
    const parts = value.split(',');
    const courseCode = parts[0];
    const course = model.offerings.filter((c) => c['course code'] === courseCode)[0];
    model.schedule.push(course);
}

function unenrollCourse(schedule, courseCode){
    schedule.schedule = schedule.schedule.filter((course) => course['course code'] != courseCode);
    schedule.publish('Dropped course.');
}

class StudentSchedule extends Publisher {
    constructor() {
        super();
        this.schedule = [];
    }

    push(course) {
        this.schedule.push(course);
        this.publish('add course');
    }
}

class ScheduleView{
    constructor(schedule) {
        this.schedule = schedule;
        this.target = document.getElementById('item_display');
        schedule.subscribe(() => this.redisplay());
    }

    redisplay() {
        console.log('Redisplaying');
        this.target.innerHTML = '';
        for (const course of this.schedule.schedule) {
            const row = makeAndFillTableRow('td', [course['course code'], course['name'], course['faculty'], course['seats open'], course['schedule'], course['credits']]);
            // Put a delete button in the first column of the row
            const button = document.createElement('button');
            button.setAttribute('type', 'button');
            button.innerText = 'Drop';
            button.addEventListener('click', ()=> unenrollCourse(this.schedule, course['course code']));
            row.insertBefore(button, row.firstElementChild);
            this.target.appendChild(row);
        }
    }


}