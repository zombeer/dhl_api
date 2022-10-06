### Here we go...

#### Approaches tested
- Requests session. Failed at live code session.
- Headless browser. Somewhat succeeded at getting data, but I'm not satisfied with quality of this solution since it can't be put into production and be scaled reasonably.
- The final one: Turned out that DHL is having bunch of APIs for different purposes. Just googled "dhl api" (:

#### Root of all evil
 [AKAMAI antibot](https://www.akamai.com/) one of the toughest to bypass in fact. I was able to get data using puppeteer, even dockerized, but it's quite unstable solution. Very slow and expensive.
 [Here's some info](https://www.zenrows.com/blog/bypass-akamai#what-is-a-bot-detection-software) on bypassing AKAMAI protection. Which is quite tricky and involving deobfuscation of JS code and researching on dozens parameters this code collects. Interesting, but time consuming (: Not worth it when API is available.

#### Final product
[API Forwarder](http://51.15.60.207:31700) can be found by link. FastAPI interface is pretty self explanatory.
[Here's sample of request](http://51.15.60.207:31700/track/?num=00340434311590220328) - responses are being cached in redis for 10 minutes since API is limited to 250 requests per day.
Overall stack of solution: `requests`, `FastAPI` + `redis cache`, `pydantic` for schemas.
In terms of improvements it's possible to replace `requests` with `httpx` in order to obtain async capabilities, but it's not a case for 250 requests per day obviously.

Added simple `k8s` manifest so you could deploy to you cluster if you wish so. Redis runs in a separated pod without any persistance, so it's not fault tolerant, but I believe it's fine at this stage (:

#### Epilogue
So... This task turned out not that much technical, more like showing "problem solving attitude"... Hopefully you'll like it (: 

Let me know, if you have any questions.