Title: TESS Data Products TEST
template: slide
save_as: data_products.html

The four cameras of TESS take consecutive images of a particular region of the sky every 2 seconds. Several data products are produced by the TESS mission from these images: <a href="https://archive.stsci.edu/missions-and-data/tess" target="_blank">Target Pixel Files (TPFs, also known as postage stamps) of selected targets, corresponding Light Curves (LCs), and Full Frame Images (FFIs)</a>. 

Each of these is created on-board the spacecraft by co-adding the individual 2-second exposures. These data products are provided in standard FITS format with multiple extensions which contain additional information on calibration, background removal, cosmic-ray rejection, and in the case of the TPFs aperture masks indicating the pixels used to extract the lightcurve. For more information, see the <a href = "https://archive.stsci.edu/missions-and-data/tess/data-products" target = "_blank"> TESS mission page at MAST </a>, the <a href="https://ui.adsabs.harvard.edu/abs/2016SPIE.9913E..3EJ/abstract" target="_blank"> TESS pipeline </a>, as well as the slideshow presented below.

Types of TESS Data Products

1 Target Pixel Files [TPF]

--Raw, target-specific data available at MAST.

--Used to create the data found in the light curve files

--For each short-cadence target in an observing sector, TESS only acquires the pixels contained within a predefined mask.

--These pixels are used to create the data found in the light curve files.

--Each target pixel file packages these pixels as a time series of images in a binary FITS table.

--The intent of these files is to provide the data necessary to perform photometry on the raw or calibrated data when needed (or desired) to understand (or improve) the automated results of the TESS pipeline.

--In the binary table, the pixel values are encoded as images.

--Each element in the binary table contains the pixels from a single cadence.

--If a target is observed in more than one sector, multiple TPFs will be created for that target but they may be made available in separate deliveries to the MAST.

--The images in the TPF will have dimensions equal to the bounding box of the pixels that were collected for that target.

--Depending on the location of the target on a CCD, a TPF may therefore contain pixels that do not contain stored data.

--TPFs will have several HDUs: a primary header, a binary table of images header and data, the aperture mask image header and data, and the cosmic ray correction binary table header and data.

--The aperture mask image provided with each TPF file indicates the pixels that were collected for the target and which of those pixels were used for photometry.

--To learn more about TPFs and how to use them please visit this page.

Here is an example TPF for TIC ZZZ.


2 Light Curve Files [LCFs or LCs]

--Flux time-series produced for each short-cadenced target (from the TPFs) using Simple Aperture Photometry (SAP).

--Used to search for transiting planets and other astrophysical phenomena.

--The flux and respective uncertainties are provided at each cadence, with NaNs filling in any missing data values.

--TESS light curves are FITS format files that contain the output of the photometric extraction and subsequent systematics removal (cotrending) performed by the SPOC algorithms.

--A single Light Curve File contains the data for one target for on observing sector.

--Identical to the case for TPFs, if a target was observed in more than one TESS sector, multiple Light Curve Files will be created but they may be made available on the MAST in separate deliveries.

--Light Curve Files will also consist of several HDUs: a primary header, the light curve photometry binary table header and data, and the aperture mask image header and data.

--The aperture mask image provided with each light curve is the same as that provided with the corresponding target TPF file.

--To learn more aboute about LCFs and how to use them please visit this page.

--Here is an example LC for TIC ZZZ.


3 Full Frame Images [FFIs]

--A collection of science and collateral pixels observed simultaneously.

--A single FFI is the full set of all science and collateral pixels across all CCDs of a given camera.

--There are 16 CCDs on the spacecraft, each of which is supported by 4 output channels.

--FITS format files containing all pixels on a single CCD

--Observational cadence of 30 minutes (Cycles 1 and 2zzz), 10 minutes (Cycles 3 and 4zzz), and 200 seconds (Cycles 5 and 6).

--FFI data is provided in three types: uncalibrated, calibrated, and uncertainty.


--Uncalibrated FFI data is provided in one file with two Header/Data Units (HDUs): a primary header and the CCD image header and data.

--Calibrated FFI data and its uncertainty are provided in a separate file with several HDUs: a primary header, the CCD calibrated image header and data, the CCD uncertainty image header and data, and the cosmic ray corrections binary table header and data.

--Cosmic Ray Mitigated FFIs are the same as FFIs except they are collected with the onboard cosmic ray mitigation enabled.

--To learn more aboute about FFIs and how to use them please visit this page.

--Here is an example FFI ZZZ.


4 TESS Data Product Workflow

--TESS identifies targets from a target list onboard the computer, and selects small pixel cut outs around those regions. Here you can see a comparison between TESS pixels and those from several larger telescopes.

--Here is a schematic diagram of one TESS CCD.

--The FFIs and pixel cut outs are downlinked. The FFIs are then sent to the MAST archive; the pixel cut outs are processed by SPOC into TPFs, and then LCFS.


5 Engineering Data [FFIs]
TESS also has several engineering data products. Scroll down to learn more about the different engineering products.


6 Cotrending Basis Vectors

--Co-trending basis vectors (CBVs) represent the set of systematic trends present in the ensemble flux data.

--Provided for each operational sector of the mission.

--Calcualted by the TESS pipeline from a Principle Component Analysis and used to mitigate systematic artifacts within the target light curves.

--Can be utilized for manual photometric correction more tailored towards the user's science.


7 Auxiliary Data Products

--Focal plane characterization files, engineering and telemetry data used to calibrate the images and determine the status of the spacecraft.

--Black level: the mean correction estimated from the virtual black pixel values. There is one metric value per cadence for each CCD readout.

--2-D black model: the expected readout of a given CCD, in counts, which is observed when no light is incident upon the detector. The model is subtracted from the raw pixel values as part of the calibration process. The model also incorporates the expected black values of collateral pixels. Each CCD has a separate 2-D black model. The size of the model is 2078 x 2136 for each CCD.

--Smear: correction for shutterless operation. The smear will be less critical for TESS than was needed for Kepler due to the use of frame-transfer in TESS.

--Gain model: linear approximation to the CCD digitizer performance, in units of photoelectrons per digitizer count. Each TESS CCD has its own gain model containing separate values for each of the 4 readouts on the CCD.

--Flat field: a model describing the pixel-to-pixel variation in response to photons. This allows the variations in individual pixel response to be removed during calibration. The flat field model is 2048 x 2048 for each CCDs.

--Linearity: a model describing the deviations from linearity of the CCD digitizers. Each CCD has its own linearity model with separate values for each of the 4 readouts on the CCD. The linearity model is used in conjunction with the gain model of each CCD to convert from a measured number of counts to a flux in photoelectrons.

--Read noise: an estimate of the variation in pixel values caused by the digitization process itself. This is separate from the noise due to Poisson variation in the number of photons collected from a target (``shot noise''). The read noise model is used in the calibration process to estimate the uncertainty in pixel values, which is incorporated into the uncertainty propagation process. Each CCD has its own read noise model with separate values for each of the 4 readouts on the CCD.

--Dark current: the mean dark current calculated from the virtual row pixel values. There is one metric value per cadence for each readout

--See MAST for a full list is available auxiliary products.


8 Collateral Data
--Includes pixels from leading and trailing virtual columns, leading and trailing masked rows, and trailing virtual rows (in units of ADC counts).

--Additional collateral data includes auxiliary instrument models which describe the calibration effects.

--Pixel calibration is performed on both the cadence pixels and Full Frame Image (FFI) pixels, and calibrated science pixel values, in photoelectrons, along with their uncertainties are archived at the MAST


9 Simulated Data

--During the development of a space mission, several End-to-End tests are conducted, which include testing the pipeline and the data transfer between different institutions.

--To do this various data products are simulated, these data can be very useful to the community, and aid potential TESS users in the development of tools and in assessing the feasibility of an investigation.

--Data for the "End-To-End 6" can be found here.


If in doubt, reach out to TESS GI Helpdesk

The TESS GI helpdesk are happy to help answer any questions, reach out on email at tesshelp@bigbang.gsfc.nasa.gov.