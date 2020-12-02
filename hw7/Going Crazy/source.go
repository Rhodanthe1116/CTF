package main
import "fmt"
func main() {

   

	var something string

	for {
		 fmt.Println("+================+
					|    Go Crazy    |
					+================+
					Say something :")

		fmt.Scanf("%s", &something)
		if something < 16 {
        	break 
        }
        fmt.Println("no ! tOo NORmAL ! yoU hAvE To Be crAzY eNoUgh BeForE GEtTING flag")
    }
}