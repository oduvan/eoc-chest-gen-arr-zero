requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'gen_arr_zero',
                js: 'genArrZero'
            }
        });
        io.start();
    }
);
