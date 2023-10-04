Title: TESS Instrument Information TEST
template: slide
save_as: instrument_information.html


Photometric performance and Technical Details


1 Typical noise levels

--The figure below shows the 1-hour Combined Differential Photometric Precision (CDPP) from TESS Sector 1.

<img src="https://heasarc.gsfc.nasa.gov/docs/tess/images/data/tess_tpf.png" width="700px"></img>

--The red points are the RMS CDPP measurements for the 15,889 light curves from Sector 1 plotted as a function of TESS magnitude.

--The blue x's are the uncertainties, scaled to a 1-hour timescale.

--The purple curve is a moving 10th percentile of the RMS CDPP measurements, and the gold curve is a moving median of the 1-hour uncertainties.

--The photometric uncertainties are dominated by pointing jitter, but the best light curves are well below the mission requirements of (1) a systematic error floor at 60 ppm and (2) an achieved CDPP at 10th magnitude of 230 ppm, which is sufficient to detect super-Earths around bright stars.

--For fainter stars around Tmag = 16, the photometric precision drops to about 1%, which is still sufficient for many astrophysical studies such as supernovae and stellar variability.

--The typical noise achieved in each individual TESS sector is described in the Data Release Notes for each sector.


2 Saturation

--The amount of charge deposited by a star of magnitude Tmag into the peak pixel depends on the fraction of the total charge in the peak pixel: this value generally ranges from 0.2 to 0.4 in the TESS images. The TESS cameras create 15,000 e-/s for a star of Tmag = 10: thus, a star of Tmag = 5 will create 3 x 106 electrons in a two-second exposure.

--For a flux fraction of 0.3, the charge in the peak pixel is 9 x 105 e-, leading to a bloom length of 5 rows; similarly, a star of Tmag = 2.5 will create a bloom of 50 rows. A key feature of the CCID-80 CCDs used on TESS is their ability to conserve charge even from very saturated stars.

--Saturation is anticipated in the central pixel at Ic = 7.5 mag. This, however, does not represent the bright limit for precise photometry.

--Excess charge from saturated pixels is conserved and spread across adjacent pixels in a CCD column until the excess reaches a CCD boundary.

--This leads to "bleed trails" extending above and below a saturated pixel, similar to what is seen for bright stars in Kepler/K2 photometry. Precision photometry can still be achieved by creating a photometric aperture that is large enough to encompass all excess charge.

--The TESS bright limit is anticipated to be Ic = 4 mag.


3 Point Spread Function

--The TESS PSF varies significantly across the focal plane due primarily to the optics.

--Instead of a PSF, TESS has a pixel response function (PRF), which represents the observed appearance of the point sources.

--The TESS PRF was created by the SPOC by fitting to micro-dithered data taken during PRF commissioning exercises. PRF models for sectors 1-3 can be found here, with sector 4 onwards here.

--Additional resources for the TESS PRF can be found on MAST.

--Physical WCS solutions can be used to convert the PRF image coordinates into the corresponding TESS CCD's. For more information about the TESS PRF see page 49 of the instrument handbook.

--Given the unusual nature of the TESS PRF, photometry of an object is typically obtained through the summation of all pixels within a given region. This region is referred to as an "aperture mask" and can be determined through the pipeline or can be selected by the user, unlike typical apertures, TESS apertures are not circular.


4 Crowding

--Because the TESS pixels are large (21 arcsec), the TESS photometry for many targets will be contaminated by nearby objects. One of the goals of the TIC is to provide the information needed to estimate the contamination in the TESS band.

--This cannot be determined accurately ahead of time because it will depend on the pixels selected for the aperture photometry of each target and the exact position of the target in the aperture.

--However, it is possible for the TIC to provide some guidance concerning the level of expected contamination, for example by providing the number of known objects and their total brightness in the TESS band for some suitable standard aperture and photometer Pixel Response Function (PRF)


5 Pointing jitter


6 Scattered light


7 Cosmic rays


8 Pointing jitter
