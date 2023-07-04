# ExoPlanet-Finder

Run this in Jupyter Notebook or Google Collab!

In this repo, we can find our own exoplants with python and the lightkurve library. Go through the basic steps of analyzing stellar timeseries data from TESS (Transiting Exoplanet Survey Satellite) to find perodic changes in brightness which may incdicate the presence of a planet in orbit of a star. There are around 9.5 million stars to look at in the dataset so you can find a planet that's never been discovered before!

Websites needed
https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html (information on exoplanets such as ID)

https://exo.mast.stsci.edu/ (to see if a exoplanet has been discovered)

To use downloader helper:
1. Find a planet by using MAST catalogs and then using advanced search
2. Take the TIC ID and paste it into exo mast
3. Using the right side search bar, use this format: TIC (your TIC id here, remove parentheses)
4. Take the Group ID
5. Paste replace the current 'product_group_id' with your group id!
6. Your computer should make the custom link for you!
