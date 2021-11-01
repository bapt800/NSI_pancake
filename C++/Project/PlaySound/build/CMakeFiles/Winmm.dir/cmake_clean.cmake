file(REMOVE_RECURSE
  "libWinmm.a"
  "libWinmm.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/Winmm.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
