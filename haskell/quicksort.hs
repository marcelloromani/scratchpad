import Data.List (partition)

main :: IO ()
main = do
  let unsorted = [1, 4, 3, 2, 90, 5, 4, 4, 4, 77]
  print ( quicksort unsorted )

quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (x:xs) = let (lesser, greater) = partition (< x) xs
                   in quicksort lesser ++ [x] ++ quicksort greater
