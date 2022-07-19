# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_void-slam-dolly_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED void-slam-dolly_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(void-slam-dolly_FOUND FALSE)
  elseif(NOT void-slam-dolly_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(void-slam-dolly_FOUND FALSE)
  endif()
  return()
endif()
set(_void-slam-dolly_CONFIG_INCLUDED TRUE)

# output package information
if(NOT void-slam-dolly_FIND_QUIETLY)
  message(STATUS "Found void-slam-dolly: 0.0.0 (${void-slam-dolly_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'void-slam-dolly' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${void-slam-dolly_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(void-slam-dolly_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${void-slam-dolly_DIR}/${_extra}")
endforeach()
