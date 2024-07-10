package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gorilla/mux"
)

type Course struct {
	CourseId    string  `json:"courseid"`
	CourseName  string  `json:"coursename"`
	CoursePrice int     `json:"courseprice"`
	Author      *Author `json:"author"`
}

type Author struct {
	Fullname string `json:"fullname"`
	Website  string `json:"website"`
}

func (c *Course) IsEmpty() bool {
	return c.CourseId == "" && c.CourseName == ""
}

var courses []Course

func main() {
	router := mux.NewRouter()
	router.HandleFunc("/", serveHome).Methods(http.MethodGet)
	router.HandleFunc("/courses", getAllCourses).Methods(http.MethodGet)
	router.HandleFunc("/courses/{id}", getOneCourse).Methods(http.MethodGet)
	router.HandleFunc("/courses", createCourse).Methods(http.MethodPost)
	router.HandleFunc("/courses/{id}", deleteCourse).Methods(http.MethodDelete)
	fmt.Println("Server listening on port 8080")
	http.ListenAndServe(":8080", router)
}

func serveHome(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1>Hello World!</h1>"))
}

func getAllCourses(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get all Courses")
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(courses)
}

func getOneCourse(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get One Course")
	params := mux.Vars(r)
	courseId := params["id"]

	var foundCourse Course
	found := false
	for _, course := range courses {
		if course.CourseId == courseId {
			foundCourse = course
			found = true
			break
		}
	}

	if found {
		json.NewEncoder(w).Encode(foundCourse)
	} else {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode("No Course Found with given Id")
	}
}

func createCourse(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Create One Course")
	w.Header().Set("Content-Type", "application/json")

	var course Course
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode("Error reading request body")
		return
	}

	if err := json.Unmarshal(body, &course); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode("Invalid JSON data in request body")
		return
	}

	if course.IsEmpty() {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode("Course Name and Course ID are required")
		return
	}

	rand.Seed(time.Now().UnixNano())
	course.CourseId = strconv.Itoa(rand.Intn(100))
	courses = append(courses, course)
	json.NewEncoder(w).Encode(course)
}

func deleteCourse(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Delete One Course")
	w.Header().Set("Content-Type", "application/json")

	params := mux.Vars(r)
	courseId := params["id"]

	var newCourses []Course
	found := false
	for _, course := range courses {
		if course.CourseId != courseId {
			newCourses = append(newCourses, course)
		} else {
			found = true
		}
	}

	if found {
		courses = newCourses
		w.WriteHeader(http.StatusNoContent)
	} else {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode("No Course Found with given Id")
	}
}
