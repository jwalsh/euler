#!/usr/bin/env clojure 
; The sequence of triangle numbers is generated by adding 
; the natural numbers. So the 7^(th) triangle number would be
; 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
;
; 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
;
; Let us list the factors of the first seven triangle numbers:
;
;      1: 1
;      3: 1,3
;      6: 1,2,3,6
;      10: 1,2,5,10
;      15: 1,3,5,15
;      21: 1,3,7,21
;      28: 1,2,4,7,14,28
;
; We can see that 28 is the first triangle number to have over
; five divisors. What is the value of the first triangle number
; to have over five hundred divisors?

(defn divisor? [b n]
  (= (rem n b) 0))

(defn triangle-number [n]
  (cond 
    (< n 1) nil
    (= n 1) 1
    :else (+ n (triangle-number (dec n)))))

(defn divisors [n]
  (cons n (filter #(divisor? % n) (range 1 (inc (/ n 2))))))


(defn num-divisors [n])

(def triangle-numbers (map triangle-number (range 1 1000)))
(println (first (filter #(> (num-divisors %) 500) triangle-numbers)))
