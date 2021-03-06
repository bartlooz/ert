/*
   Copyright (C) 2011  Statoil ASA, Norway.

   The file 'enkf_tui_main.c' is part of ERT - Ensemble based Reservoir Tool.

   ERT is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   ERT is distributed in the hope that it will be useful, but WITHOUT ANY
   WARRANTY; without even the implied warranty of MERCHANTABILITY or
   FITNESS FOR A PARTICULAR PURPOSE.

   See the GNU General Public License at <http://www.gnu.org/licenses/gpl.html>
   for more details.
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ert/util/util.hpp>
#include <ctype.h>
#include <enkf_tui_run.hpp>
#include <enkf_tui_export.hpp>
#include <enkf_tui_table.hpp>
#include <enkf_tui_fs.hpp>
#include <enkf_tui_ranking.hpp>
#include <enkf_tui_QC.hpp>
#include <enkf_tui_help.hpp>
#include <enkf_tui_misc.hpp>
#include <enkf_tui_simple.hpp>
#include <enkf_tui_workflow.hpp>

#include <ert/enkf/enkf_main.hpp>
#include "menu.hpp"


/**
   This file implements the (text based) user interface in the enkf
   system.
*/



/**
    The main loop.
*/





void enkf_tui_main_menu(void * arg) {
  enkf_main_type * enkf_main = enkf_main_safe_cast( arg );
  menu_type * menu = menu_alloc("Main menu" , "Quit" , "qQ");

  menu_add_item(menu , "Manage cases"                          , "cC" , enkf_tui_fs_menu        , enkf_main , NULL);
  menu_add_item(menu , "Run, restart or analyse experiment"    , "rR" , enkf_tui_run_menu       , enkf_main , NULL);
  menu_add_item(menu , "Rank results"                          , "aA" , enkf_tui_ranking_menu   , enkf_main , NULL);
  menu_add_item(menu , "Export data to other formats"          , "eE" , enkf_tui_export_menu    , enkf_main , NULL);
  menu_add_item(menu , "Table of results"                      , "tT" , enkf_tui_table_menu     , enkf_main , NULL);
  menu_add_item(menu , "Miscellanous"                          , "mM" , enkf_tui_misc_menu      , enkf_main , NULL);
  menu_add_item(menu , "Workflows"                             , "wW" , enkf_tui_workflow_menu  , enkf_main , NULL);
  menu_add_item(menu , "Help"                                  , "hH" , enkf_tui_help_menu_main , enkf_main , NULL);
  menu_add_item(menu , "Simple menu"                           , "sS" , enkf_tui_simple_menu    , enkf_main , NULL);
  menu_run(menu);
  menu_free(menu);
}


