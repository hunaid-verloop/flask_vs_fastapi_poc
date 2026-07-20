package main

import (
	"context"
	"log"
	"math/rand"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"
)

func sayHelloHandler(w http.ResponseWriter, r *http.Request) {
	rt := time.Duration(rand.Intn(3))
	time.Sleep(rt * time.Second)
	w.Header().Add("Content-Type", "application/json")
	w.Write([]byte(`{"message": "Hello, World!"}`))
}

func main() {
	addr := ":6000"
	srv := &http.Server{
		Addr:    addr,
		Handler: http.HandlerFunc(sayHelloHandler),
	}

	go func() {
		quit := make(chan os.Signal, 1)
		signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
		<-quit
		if err := srv.Shutdown(context.Background()); err != nil {
			log.Printf("HTTP server Shutdown: %v", err)
		}

	}()
	err := srv.ListenAndServe()
	log.Println("Listening on port", addr)

	if err != nil && err != http.ErrServerClosed {
		log.Fatalf("HTTP server ListenAndServe: %v", err)
	}
}
