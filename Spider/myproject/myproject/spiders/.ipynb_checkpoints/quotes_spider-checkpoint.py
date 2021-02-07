{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scrapy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class QuoteSpider(scrapy.spider):\n",
    "    name = \"quotes_spider\"\n",
    "    \n",
    "    def start_request(self):\n",
    "        \n",
    "        urls = [\"https://quotes.toscrape.com/page/1/\",\n",
    "              \"https://quotes.toscrape.com/page/2/\",\n",
    "              \"https://quotes.toscrape.com/page/3/\"]\n",
    "        \n",
    "        for url in urls:\n",
    "            yeild scrapy.request(url = ulr,callback=self.parse)\n",
    "            \n",
    "    def parse(self,response):\n",
    "        page_id = response.url.split(\"/\")[-2]\n",
    "        filename = \"quotes-%s.html\"%page_id\n",
    "        with open(filename,\"w\") as f:\n",
    "            f.write(response.body())\n",
    "        self.log('Saved file %s',filename)\n",
    "        \n",
    "        \n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
