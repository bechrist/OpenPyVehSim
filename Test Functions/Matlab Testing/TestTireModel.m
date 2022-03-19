function Out = TestTireModel(In,Param)
%% P4 Pacejka Testing Model
% [Fx, Fy] = fcn(Alpha, Kappa, Fz)
%
% Notes:
% - To be used for platform development not design
% - Model derived from:
%   - RVCD (Milliken & Milliken)
%   - Tire & Vehicle Dynamics (Pacejka)
% - Model default parameters set in range of FSAE Tires
%
% Blake Christierson (bechristierson@sbcglobal.net)
% 25 Feb 2022

%% Parsing
p = inputParser;
    
validPosScalar = @(x) isnumeric(x) && isscalar(x) && (x > 0);
validFunction = @(x) isa(x, 'function_handle');

addRequired(p, 'Prob', validFunction);
addRequired(p, 'params', @isvector);
addRequired(p, 'x', @isvector);

addParameter(p, 'tol', 10^-6, validPosScalar);
addParameter(p, 'maxIter', 50, validPosScalar);

parse(p, Prob, params, x, varargin{:});

end

