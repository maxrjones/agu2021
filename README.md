# PyGMT: An open-source Python library for geospatial processing, analysis, and visualization
2021 AGU Fall Meeting Presentation about PyGMT

|    |Info|
|---:|:---|
| Session | [IN55C - Open-Source Software, Notebooks, and FAIR Software I eLightning](https://agu.confex.com/agu/fm21/meetingapp.cgi/Session/140226) |
| Abstract | [IN55C-08](https://agu.confex.com/agu/fm21/meetingapp.cgi/Paper/916483) |
| Authors | [Meghan Jones](https://github.com/meghanrjones), [Michael Grund](https://github.com/michaelgrund), [William Schlitzer](https://github.com/willschlitzer), [Wei Ji Leong](https://github.com/weiji14), [Dongdong Tian](https://seisman.info/), [Jiayuan Yao](https://github.com/core-man), [Leonardo Uieda](http://www.leouieda.com/) | 
| When | Friday, 17 December 2021 16:21 - 16:24 CST (UTC-6) |
| Where | AGU Conference Online Session |

## Abstract

PyGMT is an open-source Python package for geospatial data processing, analysis, and visualization. PyGMT is designed to integrate smoothly with scientific Python packages (e.g., NumPy, pandas, xarray, GeoPandas), support rich display in Jupyter notebooks, and improve access to the Generic Mapping Tools (GMT) by providing a user-friendly interface to the GMT C API. Here, we showcase PyGMT’s strengths in supporting Findable, Accessible, Interoperable, and Reusable (FAIR) workflows for processing geospatial data and producing publication quality maps and figures. We provide an overview of the features available in PyGMT, including plotting methods, operations on tabular data (e.g., data gridding), and operations on grids (e.g., grid filtering) as well as outline PyGMT’s development process, including testing, versioning, and archival. We will use an online notebook to share a few common use-cases for PyGMT, including gridding geospatial tabular data, plotting the gridded data using one of 30+ map projections with GMT’s fast generation of a directional gradient grid for illumination, and adding map embellishments such as insets, scale bars, and legends. The growing PyGMT team strives to nurture a welcoming community that supports and values contributions of all forms, including documentation, code, teaching, helping newcomers, and outreach. We will discuss PyGMT’s approach to fostering our community and our future plans, including simplifying the syntax, improving the integration with ObsPy, and supporting animations.

## Plain-language summary

Processing and plotting spatial data are essential tasks across many scientific disciplines. PyGMT is a Python package designed to help scientists accomplish these tasks. PyGMT provides a Python interface to the Generic Mapping Tools (GMT) software, which is a command line toolbox for processing data, generating publication-quality figures, and making animations. PyGMT is able to support a remarkable number of features by leveraging GMT’s 30+ years of continuous development. At the same time, PyGMT brings a fresh perspective to GMT by following the guiding principles of the Python language, supporting interactive computing, and allowing access to GMT’s features while using other popular Python packages, such as xarray, pandas, and NumPy.

## License

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

## Acknowledgements

The development of PyGMT has been supported by NSF grants
[OCE-1558403](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1558403) and
[EAR-1948603](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1948602).
M.R. Jones has been supported by [EAR-1948602](https://nsf.gov/awardsearch/showAward?AWD_ID=19486020).
PyGMT has benefited from the contributions of [numerous developers](https://github.com/GenericMappingTools/pygmt/blob/main/AUTHORS.md)
and [community members](https://forum.generic-mapping-tools.org/).