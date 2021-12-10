# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Plot focal mechanisms using PyGMT
#
# Based on example by Federico Esteban at https://docs.generic-mapping-tools.org/latest/animations/anim14.html.
#
# Data are from the [Global Centroid-Moment-Tensor (CMT)](https://www.globalcmt.org/) Project:
# * Dziewonski, A. M., T.-A. Chou and J. H. Woodhouse, Determination of earthquake source parameters from waveform data for studies of global and regional seismicity, J. Geophys. Res., 86, 2825-2852, 1981. doi:10.1029/JB086iB04p02825
# * Ekström, G., M. Nettles, and A. M. Dziewonski, The global CMT project 2004-2010: Centroid-moment tensors for 13,017 earthquakes, Phys. Earth Planet. Inter., 200-201, 1-9, 2012. doi:10.1016/j.pepi.2012.04.002)

# %%
import pandas as pd
import pygmt

# %%
# Select points for the cross section
profile = pd.DataFrame(data={"x": [-75.02, -63.65], "y": [-33.5, -31]})
profile.to_csv("profile.txt", sep=",", header=None, index=False)
# np.array([[-111.6, -43.0], [-113.3, -47.5]])
# profile.tofile('profile.txt', sep=',')
# Extract data inside/outside profile
pygmt.select(
    data="@GCMT_1976-2017_meca.gmt",
    L="profile.txt+d100k+p",
    coltypes="g",
    outfile="GCMT_1976-2017_meca_in.txt",
)
pygmt.select(
    data="@GCMT_1976-2017_meca.gmt",
    L="profile.txt+d100k+p",
    coltypes="g",
    reverse="l",
    outfile="GCMT_1976-2017_meca_out.txt",
)

# %%
# Create figure
fig = pygmt.Figure()
# Adjust figure configuration
pygmt.config(
    GMT_VERBOSE="e",
    FONT_ANNOT_PRIMARY="18p",
    MAP_FRAME_PEN="thin,black",
    MAP_GRID_PEN="faint,gray",
)
# Create a colormap for earthquake depths
pygmt.makecpt(series=[0, 190], cmap="hot", reverse=True)
# Plot a basemap for the focal mechanism cross-sections
fig.basemap(
    region=[0, 1100, 0, 190],
    projection="X22.73i/-2.7i",
    frame=["g25", "wESn", 'xaf+l"Distance (km)"', 'yaf+l"Depth (km)"'],
)
# Plot the focal mechanism cross-sections
with pygmt.clib.Session() as lib:
    file_context = lib.virtualfile_from_data(
        check_kind="vector",
        data="GCMT_1976-2017_meca_in.txt",
        x=None,
        y=None,
        extra_arrays=None,
    )
    with file_context as fname:
        lib.call_module(
            "coupe",
            f"{fname} -Aa-75.02/-33.5/-63.65/-31+w100k -Q -Sc0.5c+f0 -C -Wfaint",
        )
# Shift the plot origin to create a new subplot
fig.shift_origin(yshift="h+0.3i")
# Plot earth relief data for the region
fig.grdimage(
    grid="@earth_relief_10m",
    cmap="oleron",
    shading="+nt1.2",
    region=[-75.1, -63, -34.44, -30.35],
    projection="M22.73i",
    frame=["wsNE", "a2f1"],
)
# Create a colormap for earthquake depths
pygmt.makecpt(series=[0, 190], cmap="hot", reverse=True)
# Plot the earthquake focal mechanisms
fig.meca(spec="GCMT_1976-2017_meca_in.txt", C=True, convention="gcmt", scale="0.5c+f0")
fig.meca(spec="GCMT_1976-2017_meca_out.txt", convention="gcmt", scale="0.5c+f0")
# Add citations
fig.text(
    text=r"Based on GMT Animation 14 by F. Esteban (https://youtu.be/Wk58r72g_nk)",
    position="cBR+jBR",
    font="16p,Helvetica,white",
    offset="-0.25i/0.6i",
    no_clip=True,
)
fig.text(
    text=r"Data from the Global Centroid-Moment-Tensor (CMT) Project (Ekström et al., 2012)",
    position="cBR+jBR",
    font="16p,Helvetica,white",
    offset="-0.25i/0.25i",
    no_clip=True,
)  # Display the figure
# Display the figure
fig.show()

# %%
# Save the figure
fig.savefig("figures/focal_mechanisms.png")
