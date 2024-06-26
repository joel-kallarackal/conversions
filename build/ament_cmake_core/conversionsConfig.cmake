# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_conversions_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED conversions_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(conversions_FOUND FALSE)
  elseif(NOT conversions_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(conversions_FOUND FALSE)
  endif()
  return()
endif()
set(_conversions_CONFIG_INCLUDED TRUE)

# output package information
if(NOT conversions_FIND_QUIETLY)
  message(STATUS "Found conversions: 0.0.0 (${conversions_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'conversions' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${conversions_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(conversions_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${conversions_DIR}/${_extra}")
endforeach()
