from newspaper import Article, ArticleException
from progress.bar import Bar
import catchBias
import catchCategory
def analyzerURL(rawURL):

    URLs = rawURL.splitlines()
    failedURL = []
    lines = sum(1 for line in URLs)
    progress = Bar("Downloading...", max=lines, suffix="%(percent).2f%% - %(eta)ds")
    processedURL = []
    for row in URLs:
        URLname = row
        if row is None:
            progress.next()
            continue

        try:
            article = Article(row)
            article.download()
            article.parse()
            if article.text is None:
                print(f"{row} - no article text found\n")
                progress.next()
                continue
            row = article.text
        except ArticleException:
            print(f"Failed to Load File {row}")
            failedURL.append(row)
            progress.next()
            continue
        biasResult = catchBias.getBias(row)
        categoryResult = catchCategory.getCategory(row)
        processedURL.append([URLname,categoryResult,biasResult])
        progress.next()
    progress.finish()
    return processedURL
