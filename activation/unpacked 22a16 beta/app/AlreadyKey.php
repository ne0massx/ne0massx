<?php
namespace app\forms;

use std, gui, framework, app;


class AlreadyKey extends AbstractForm
{

    /**
     * @event button.action 
     */
    function doButtonAction(UXEvent $e = null)
    {    
        $text = $this->edit->text;
        $this->label4->text = $text;
        if ($text == 542873) {
            $text2 = $this->editAlt->text;
            $this->label6->text = $text2;
        }
        else {
            $text3 = $this->edit3->text;
            $this->label6->text = $text3;
            
        }
    }


}
