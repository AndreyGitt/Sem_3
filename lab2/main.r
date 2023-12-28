levenshtein_distance <- function(s1, s2) {
  n <- nchar(s1)
  m <- nchar(s2)
  mat <- matrix(0, n + 1, m + 1)

  for (i in 1:(n + 1)) {
    mat[i, 1] <- i
  }

  for (j in 1:(m + 1)) {
    mat[1, j] <- j
  }

  for (i in 2:(n + 1)) {
    for (j in 2:(m + 1)) {
      if (substring(s1, i - 1, i - 1) == substring(s2, j - 1, j - 1)) {
        mat[i, j] <- mat[i - 1, j - 1]
      } else {
        mat[i, j] <- 1 + min(mat[i - 1, j], min(mat[i, j - 1], mat[i - 1, j - 1]))
      }
    }
  }
  return(mat[n + 1, m + 1])
}

# Пример использования
# Австрия Австралия 2
# кот скот 1
s1 <- "кот"
s2 <- "скот"
distance <- levenshtein_distance(s1, s2)
cat("Расстояние Левенштейна между '", s1, "' и '", s2, "' = ", distance-1)
print("\n")
s1 <- "Австрия"
s2 <- "Австралия"
distance <- levenshtein_distance(s1, s2)
cat("Расстояние Левенштейна между '", s1, "' и '", s2, "' = ", distance-1)

