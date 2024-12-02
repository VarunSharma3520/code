package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
)

const myurl = "http://localhost:27001"

func api() {
	response, err := http.Get(myurl)
	if err != nil {
		panic(err)
	}
	fmt.Println(response)
	defer response.Body.Close()
	databytes, err := io.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(databytes))
	urlParesing, err := url.Parse(myurl)
	if err != nil {
		panic(err)
	}

	fmt.Println(urlParesing.Host)
  postBody := strings.NewReader(`
    {
    "name":"cybro",
    "age":"undefined"
    }
    `)
  postResponse, err := http.Post(myurl+"/post","application/json",postBody)
  if err != nil {
    panic(err)
  }
  content, err := io.ReadAll(postResponse.Body)

  if err != nil {
    panic(err)
  }

  strcontent := string(content)
  fmt.Println(strcontent)


}
