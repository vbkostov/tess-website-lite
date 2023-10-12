Title: TESS Summary
template: slide
save_as: summary.html

The TESS mission provides the community with an opportunity to make ground-breaking discoveries in the field of exoplanets, astrophysics and planetary science. A summary of the technical details that proposers should be aware of can be found here.

A description of the overall mission can be found in Ricker et al. 2015. Brief descriptions of the mission operations, including the TESS orbit, field-of-view, time-sampling, and observing strategy, can be found on the objectives and primary mission pages.

This website as well as the TESS Instrument Handbook and Data Release Notes should be consulted for the latest information regarding observing with TESS.


<button type="button" class="btn btn-lg btn-secondary" data-bs-toggle="popover" data-bs-placement="bottom"
  data-bs-title="What's TESS doing right now?"
  data-bs-content="TESS is currently DOING SOMETHING for SECTOR, and is pointing towards A LOCATION. Click here to go SOMEWHERE ELSE.">Where's
  TESS now?</button>

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}
</style>
</head>

<body>

<button type="button" class="collapsible">Mission objectives</button>
<div class="content">
    The Transiting Exoplanet Survey Satellite (TESS) is a NASA-sponsored Astrophysics Explorer-class mission that is performing a near all-sky survey to search for planets transiting nearby stars. The primary goal of TESS is to discover planets smaller than Neptune that transit stars bright enough to enable follow-up spectroscopic observations that can provide planet masses and atmospheric compositions
</div>

<button type="button" class="collapsible">Launch and orbit</button>
<div class="content">
    TESS launched on April 18, 2018 from Cape Canaveral Air Force Station aboard a SpaceX Falcon 9 rocket. TESS is the first NASA Astrophysics satellite mission to be launched under a contract with SpaceX.

    TESS observes from a unique elliptical high Earth orbit (HEO) that provides an unobstructed view of its field to obtain continuous light curves and a more stable platform for precise photometry than the low Earth orbit. The launch carried the observatory to parking orbit inclined by 28.5 degrees. The high Earth orbit was achieved through a series of propulsion system burns and a lunar flyby. Two burns raised the orbit apogee to 400,000 km, one at perigee of the first phasing orbit and another at perigee of the second phasing orbit. Another small adjustment was made before a lunar gravitational assist raised the ecliptic inclination to ~40 degrees. The final apogee and ~13.7 day orbital period were achieved through a final period-adjustment maneuver after the lunar flyby. Final orbit was achieved around 60 days after launch and regular science operations began July 25, 2018.

    The nominal perigee and apogee of of the elliptical orbit are 17 Earth radii and 59 Earth radii, respectively. The exact orbital period varies between 12-15 days. The orbit places the spacecraft in a 2:1 resonance with the Moon and is inclined with respect to the Ecliptic plane. This avoids lengthy eclipses of the Earth and Moon through the FOV. The large apogee and perigee keep the spacecraft above the Earth's radiation belts and provide a nearly constant thermal environment for the stable -75 degrees C operation of the CCDs. The orbit is operationally stable due to the Moon leading or lagging the apogee by about 90 degrees, effectively averaging out lunar perturbations. The period and semi-major axis are relatively stable, with long term inclination and eccentricity exchanges over periods of 8-12 years. There are additional short term perturbations caused by the Sun with a period of 6 months. The TESS high Earth orbit is stable for decades or longer and requires no propulsion for station-keeping.

    At the TESS orbit perigee (varies between 12-20 Earth radii), science operations are interrupted for no more than 16 h to point TESS's antenna toward Earth, downlink data, and resume observing. This timeframe includes the nominal 4-h period for Ka-band science data downlink using NASA's Deep Space Network (DSN). TESS will also use its hydrazine thrusters to unload angular momentum built up from solar photon pressure at perigee and throughout the orbit.
    <img class="img-responsive" style="max-width:75%;" src="images/data/tess_orbit_Winnpresentation.jpg"></img>
</div>

<button type="button" class="collapsible">Science operations</button>
<div class="content">

</div>



<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>

</body>
</html>