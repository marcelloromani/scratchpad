import System.IO ( hFlush, stdout )

main :: IO ()
main = do
    putStr "What is your name? "
    hFlush stdout
    name <- getLine
    putStrLn("Hello " ++ name)
