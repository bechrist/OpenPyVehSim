classdef (Abstract) VehicleComponent
    %VEHICLECOMPONENT - s
    %   Detailed explanation goes here
    
    properties (Abstract)
        States
        Parameters
        
    end
    
    methods (Abstract)
        function obj = VehicleComponent(inputArg1,inputArg2)
            %VEHICLECOMPONENT Construct an instance of this class
            %   Detailed explanation goes here
            obj.Property1 = inputArg1 + inputArg2;
        end
        
        function outputArg = method1(obj,inputArg)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            outputArg = obj.Property1 + inputArg;
        end
    end
end

