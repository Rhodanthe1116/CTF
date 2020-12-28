package main

import (
    "fmt"
    s "strings"
)

var p = fmt.Println

func main() {

  
	var a = s.Split("x,,,,,x", ",")
	p("Split:     ", a)
	
}